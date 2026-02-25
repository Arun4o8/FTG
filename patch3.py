import codecs

file_path = "round_two.html"
with codecs.open(file_path, "r", "utf-8") as f:
    content = f.read()

# Add Spot the Defect and Missing Modules to questionsPool
spot_the_error = r"""        const questionsPool = [
            {
                title: "Spot the Defect",
                desc: "The program is supposed to calculate and print the Factorial of 5 but it is heavily broken with exactly 10 errors. Fix them all!",
                example: "Output: Factorial is 120",
                boilerplates: {
                    c: "#include <stdio.h>\nint main( { \n    int n = 5\n    int fact = 0; \n    for (int i=1, i<=n, i++) { \n        fact = fact * i \n    }\n    prntf(\"Factorial is %d\\n\", factorial); \n    if (fact = 120) { \n        printf(\"Correct\") \n    }\n    return 0 \n}",
                    java: "public class Main {\n    public void main(String[] args) { \n        int n = 5 \n        int fact = 0; \n        for (int i=1, i<=n, i++) { \n            fact = fact * i \n        }\n        System.out.putln(\"Fac: \" + factorial); \n        if (fact = 120) { \n            System.out.printl(\"Correct\") \n        }\n    }\n}",
                    python: "def calc_factorial():\n    n = 5\n    fact = 0 \n    for i in range(1, n) \n        fact = fact * i\n    print(\"Factorial is \" + factorial) \n    if fact = 120 \n        print(\"Correct\" \n    else \n        print(Wrong)\n\ncalc_factorial()"
                }
            },
            {
                title: "Missing Modules",
                desc: "Fill in the `____` blanks inside the loops so the logic accurately generates the first 5 Fibonacci numbers (0 1 1 2 3).",
                example: "Output: 0 1 1 2 3",
                boilerplates: {
                    c: "#include <stdio.h>\nint main() {\n    int n1=0, n2=1, n3, i, count=5;\n    printf(\"%d %d\", n1, n2);\n    for(i=2; i<count; ____) {\n        n3 = n1 + n2;\n        printf(\" %d\", n3);\n        n1 = ____;\n        n2 = ____;\n    }\n    return 0;\n}",
                    java: "public class Main {\n    public static void main(String[] args) {\n        int n1=0, n2=1, n3, i, count=5;\n        System.out.print(n1 + \" \" + n2);\n        for(i=2; i<count; ____) {\n            n3 = n1 + n2;\n            System.out.print(\" \" + n3);\n            n1 = ____;\n            n2 = ____;\n        }\n    }\n}",
                    python: "def print_fibo():\n    n1, n2 = 0, 1\n    count = 5\n    print(n1, n2, end=\" \")\n    for i in range(2, count):\n        n3 = n1 + n2\n        print(n3, end=\" \")\n        n1 = ____\n        n2 = ____\n\nprint_fibo()"
                }
            },"""

load_logic_start = """            const shuffled = [...questionsPool].sort(() => 0.5 - Math.random());
            selectedQuestions.push(...shuffled.slice(0, 5));"""
load_logic_replacement = """            // guarantee spot the defect is always here
            const spotDefect = questionsPool.find(q => q.title === "Spot the Defect");
            const missingMod = questionsPool.find(q => q.title === "Missing Modules");
            const others = questionsPool.filter(q => q.title !== "Spot the Defect" && q.title !== "Missing Modules").sort(() => 0.5 - Math.random());
            if (spotDefect) selectedQuestions.push(spotDefect);
            if (missingMod) selectedQuestions.push(missingMod);
            const remaining = 5 - selectedQuestions.length;
            if (remaining > 0) {
                selectedQuestions.push(...others.slice(0, remaining));
            }"""

runcode_start = """                if (result.status.id === 3) {
                    if (codeEditor.length > 25) {"""
runcode_replacement = """                if (result.status.id === 3) {
                    let success = false;
                    const qIndex = questionNumber - 1;
                    const currentQuestion = selectedQuestions[qIndex];
                    if (currentQuestion && currentQuestion.title === "Spot the Defect") {
                        const code = codeEditor.toLowerCase().replace(/\s/g, '');
                        if (langValue === 'c') success = code.includes("main()") && !code.includes("prntf") && code.includes("==") && !code.includes("factorial)");
                        else if (langValue === 'java') success = code.includes("static") && code.includes("==") && !code.includes("putln") && !code.includes("printl") && !code.includes("factorial)");
                        else if (langValue === 'python') success = code.includes("fact=1") && code.includes("==") && code.includes("wrong");
                        else success = false;
                        
                        if (success && actualOutput.includes("120")) {
                            success = true;
                            validationMessage = "\\n> [+] System Analysis: Target output achieved. All defects neutralized.";
                        } else {
                            success = false;
                            validationMessage = "\\n> [-] System Analysis: Executed, but logic still incorrect or defects remain.";
                        }
                    } else if (currentQuestion && currentQuestion.title === "Missing Modules") {
                        const code = codeEditor.replace(/\s/g, '');
                        if (langValue === 'c' || langValue === 'java') success = (!code.includes("____")) && code.includes("i++") && (code.includes("n1=n2;") || code.includes("n1=n2")) && (code.includes("n2=n3;") || code.includes("n2=n3"));
                        else if (langValue === 'python') success = (!code.includes("____")) && code.includes("n1=n2") && code.includes("n2=n3");
                        else success = false;

                        if (success && actualOutput.includes("0 1 1 2 3")) {
                            success = true;
                            validationMessage = "\\n> [+] System Analysis: Modules linked successfully.";
                        } else {
                            success = false;
                            validationMessage = "\\n> [-] System Analysis: Blanks filled, but output does not match first 5 fibonacci.";
                        }
                    } else {
                         success = codeEditor.length > 25;
                         validationMessage = success ? "\\n> [+] System Analysis: Code compiled successfully." : "\\n> [-] System Analysis: Logic seems too brief. Expand logic.";
                    }

                    if (success) {"""

content = content.replace("        const questionsPool = [", spot_the_error)
content = content.replace(load_logic_start, load_logic_replacement)
content = content.replace(runcode_start, runcode_replacement)

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(content)

print("Patch applied for Spot the error.")
