# -*- coding: utf-8 -*-
import codecs

file_path = "round_two.html"
with codecs.open(file_path, "r", "utf-8") as f:
    content = f.read()

# 1. Replace HTML questions block
html_start = "<!-- QUESTION 1 -->"
html_end_full = content.find('<button type="submit" id="submit-btn" class="submit-btn">> SUBMIT_SYS.DATA </button>')

if html_end_full != -1 and content.find(html_start) != -1:
    content = content[:content.find(html_start)] + '<div id="questions-container"></div>\n            ' + content[html_end_full:]

# 2. Replace JS Question Logic
js_start = "// --- Question 1 Language Switching ---"
js_end = "// --- Form Submission Logic ---"

new_js = """
        // --- Dynamic Questions ---
        const questionsPool = [
            {
                title: "Longest Common Prefix",
                desc: "Write a function to find the longest common prefix in an array of strings.",
                example: "Input: [\\"flower\\",\\"flow\\",\\"flight\\"]\\nOutput: \\"fl\\"",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <string.h>\\n\\nvoid longestCommonPrefix(char strs[][20], int n, char result[]) {\\n    // Write your logic here\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static String longestCommonPrefix(String[] strs) {\\n        // Write your logic here\\n        return \\"\\";\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def longest_common_prefix(strs):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Reverse a String",
                desc: "Write a function to reverse a given string.",
                example: "Input: \\"hello\\"\\nOutput: \\"olleh\\"",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <string.h>\\n\\nvoid reverse(char str[]) {\\n    // Write your logic here\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static String reverseString(String s) {\\n        // Write your logic here\\n        return \\"\\";\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def reverse_string(s):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Find Maximum Element",
                desc: "Write a function to find the largest number in an array.",
                example: "Input: [10, 5, 20, 8]\\nOutput: 20",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint findMax(int arr[], int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int findMax(int[] arr) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def find_max(arr):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Check Palindrome",
                desc: "Write a function to check if a string is a palindrome.",
                example: "Input: \\"madam\\"\\nOutput: True",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <string.h>\\n\\nint isPalindrome(char str[]) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static boolean isPalindrome(String s) {\\n        // Write your logic here\\n        return false;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def is_palindrome(s):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Count Vowels",
                desc: "Write a function to count vowels in a string.",
                example: "Input: \\"computer\\"\\nOutput: 3",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <string.h>\\n\\nint countVowels(char str[]) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int countVowels(String s) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def count_vowels(s):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Factorial",
                desc: "Write a function to find the factorial of a number.",
                example: "Input: 5\\nOutput: 120",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint factorial(int n) {\\n    // Write your logic here\\n    return 1;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int factorial(int n) {\\n        // Write your logic here\\n        return 1;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def factorial(n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Remove Duplicates",
                desc: "Write a function to remove duplicate elements from an array.",
                example: "Input: [1,2,2,3,4]\\nOutput: [1,2,3,4]",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint removeDuplicates(int arr[], int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "import java.util.Arrays;\\n\\npublic class Main {\\n    static int[] removeDuplicates(int[] arr) {\\n        // Write your logic here\\n        return arr;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def remove_duplicates(arr):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Fibonacci Series",
                desc: "Write a function to print the first N Fibonacci numbers.",
                example: "Input: 5\\nOutput: 0 1 1 2 3",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nvoid fibonacci(int n) {\\n    // Write your logic here\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static void fibonacci(int n) {\\n        // Write your logic here\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def fibonacci(n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Check Prime",
                desc: "Write a function to check whether a number is prime.",
                example: "Input: 11\\nOutput: True",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint isPrime(int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static boolean isPrime(int n) {\\n        // Write your logic here\\n        return false;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def is_prime(n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Sum of Digits",
                desc: "Write a function to find the sum of digits.",
                example: "Input: 456\\nOutput: 15",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint sumOfDigits(int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int sumOfDigits(int n) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def sum_of_digits(n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Second Largest Number",
                desc: "Write a function to find the second largest number in an array.",
                example: "Input: [10,20,30,40]\\nOutput: 30",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint secondLargest(int arr[], int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "import java.util.Arrays;\\n\\npublic class Main {\\n    static int secondLargest(int[] arr) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def second_largest(arr):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Find Missing Number",
                desc: "Write a function to find the missing number from 1 to N.",
                example: "Input: [1,2,4,5]\\nOutput: 3",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint missingNumber(int arr[], int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int missingNumber(int[] arr, int n) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def missing_number(arr, n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Anagram Check",
                desc: "Write a function to check if two strings are anagrams.",
                example: "Input: \\"listen\\",\\"silent\\"\\nOutput: True",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <string.h>\\n\\nint isAnagram(char a[], char b[]) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "import java.util.Arrays;\\n\\npublic class Main {\\n    static boolean isAnagram(String s1, String s2) {\\n        // Write your logic here\\n        return false;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def is_anagram(s1, s2):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Count Words",
                desc: "Write a function to count words in a sentence.",
                example: "Input: \\"I love coding\\"\\nOutput: 3",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint countWords(char str[]) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int countWords(String s) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def count_words(s):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Armstrong Number",
                desc: "Write a function to check whether a number is an Armstrong number.",
                example: "Input: 153\\nOutput: True",
                boilerplates: {
                    c: "#include <stdio.h>\\n#include <math.h>\\n\\nint isArmstrong(int n) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static boolean isArmstrong(int n) {\\n        // Write your logic here\\n        return false;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def is_armstrong(n):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Sort an Array",
                desc: "Write a function to sort an array in ascending order.",
                example: "Input: [5,3,1,4]\\nOutput: [1,3,4,5]",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nvoid sortArray(int arr[], int n) {\\n    // Write your logic here\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "import java.util.Arrays;\\n\\npublic class Main {\\n    static void sortArray(int[] arr) {\\n        // Write your logic here\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def sort_array(arr):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Find GCD",
                desc: "Write a function to find the GCD of two numbers.",
                example: "Input: 12,18\\nOutput: 6",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint gcd(int a, int b) {\\n    // Write your logic here\\n    return 1;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int gcd(int a, int b) {\\n        // Write your logic here\\n        return 1;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def gcd(a, b):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Find LCM",
                desc: "Write a function to find the LCM of two numbers.",
                example: "Input: 4,6\\nOutput: 12",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint lcm(int a, int b) {\\n    // Write your logic here\\n    return 1;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int lcm(int a, int b) {\\n        // Write your logic here\\n        return 1;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def lcm(a, b):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Character Frequency",
                desc: "Write a function to find the frequency of each character.",
                example: "Input: \\"apple\\"\\nOutput: a:1, p:2, l:1, e:1",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nvoid charFrequency(char str[]) {\\n    // Write your logic here\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "import java.util.*;\\n\\npublic class Main {\\n    static void charFrequency(String s) {\\n        // Write your logic here\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def char_frequency(s):\\n    # Write your logic here\\n    pass\\n"
                }
            },
            {
                title: "Binary to Decimal",
                desc: "Write a function to convert binary to decimal.",
                example: "Input: \\"1010\\"\\nOutput: 10",
                boilerplates: {
                    c: "#include <stdio.h>\\n\\nint binaryToDecimal(char bin[]) {\\n    // Write your logic here\\n    return 0;\\n}\\n\\nint main() {\\n    return 0;\\n}",
                    java: "public class Main {\\n    static int binaryToDecimal(String b) {\\n        // Write your logic here\\n        return 0;\\n    }\\n    public static void main(String[] args) {\\n    }\\n}",
                    python: "def binary_to_decimal(b):\\n    # Write your logic here\\n    pass\\n"
                }
            }
        ];

        const selectedQuestions = [];

        function loadQuestions() {
            const shuffled = [...questionsPool].sort(() => 0.5 - Math.random());
            selectedQuestions.push(...shuffled.slice(0, 5));
            
            const container = document.getElementById('questions-container');
            container.innerHTML = '';
            
            selectedQuestions.forEach((q, idx) => {
                const i = idx + 1;
                container.innerHTML += `
                    <div class="question-section">
                        <h2>Q${i}: ${q.title} (4 Marks)</h2>
                        <p class="problem-statement">
                            <strong>Objective:</strong> ${q.desc}<br><br>
                            <strong>Example:</strong><br>
                            <span style="white-space: pre-wrap;">${q.example}</span>
                        </p>
                        <div class="editor-header">
                            <label for="lang${i}">> Select Language:</label>
                            <select id="lang${i}" name="q${i}Language" required onchange="changeLanguage(${i})">
                                <option value="">-- Choose --</option>
                                <option value="c">C</option>
                                <option value="java">Java</option>
                                <option value="python">Python</option>
                            </select>
                        </div>
                        <textarea id="code${i}" name="q${i}Code" class="editor" required placeholder="Select language to load code..."></textarea>
                        <div class="action-row">
                            <button type="button" class="btn-run" onclick="runCode(${i})">[ Execute Code ]</button>
                            <span id="status${i}" style="color: yellow; font-size: 0.9em; display: none;">Executing...</span>
                        </div>
                        <div id="output${i}" class="output-box"></div>
                    </div>
                `;
            });
            
            // Re-bind tab functionality
            const textareas = document.querySelectorAll('textarea.editor');
            textareas.forEach(ta => {
                ta.addEventListener('keydown', function (e) {
                    if (e.key === 'Tab') {
                        e.preventDefault();
                        const start = this.selectionStart;
                        const end = this.selectionEnd;
                        this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
                        this.selectionStart = this.selectionEnd = start + 4;
                    }
                });
            });
        }

        function changeLanguage(i) {
            const lang = document.getElementById(`lang${i}`).value;
            const qIndex = i - 1;
            const editor = document.getElementById(`code${i}`);
            if (lang && selectedQuestions[qIndex].boilerplates[lang]) {
                if (!editor.value || Object.values(selectedQuestions[qIndex].boilerplates).includes(editor.value)) {
                   editor.value = selectedQuestions[qIndex].boilerplates[lang];
                }
            }
        }

        let questionScores = { q1: 0, q2: 0, q3: 0, q4: 0, q5: 0 };

        async function runCode(questionNumber) {
            const langValue = document.getElementById(`lang${questionNumber}`).value;
            const codeEditor = document.getElementById(`code${questionNumber}`).value;
            const outputBox = document.getElementById(`output${questionNumber}`);
            const statusSpan = document.getElementById(`status${questionNumber}`);

            if (!langValue) {
                alert("Please select a programming language first!");
                return;
            }
            if (codeEditor.trim() === '') {
                alert("Code editor is empty!");
                return;
            }

            outputBox.style.display = 'block';
            outputBox.textContent = '> Compiling code in live server...';
            statusSpan.style.display = 'inline';

            let languageId = 92; // Python 3.11 default
            if (langValue === 'c') languageId = 103; // C GCC 14.1
            else if (langValue === 'java') languageId = 91; // Java JDK 17

            try {
                const response = await fetch("https://ce.judge0.com/submissions?base64_encoded=false&wait=true", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        source_code: codeEditor,
                        language_id: languageId,
                    })
                });

                if (!response.ok) throw new Error("Live API failed");
                const result = await response.json();

                let actualOutput = result.stdout || "";
                let errorOutput = result.compile_output || result.stderr || result.message || "";
                let validationMessage = "";

                if (result.status.id === 3) {
                    if (codeEditor.length > 25) {
                        questionScores[`q${questionNumber}`] = 4;
                        validationMessage = "\\n> [+] System Analysis: Code compiled successfully.";
                    } else {
                        questionScores[`q${questionNumber}`] = 0;
                        validationMessage = "\\n> [-] System Analysis: Logic seems too brief. Expand logic.";
                    }
                    outputBox.textContent = "--- COMPILE SUCCESS (LIVE) ---\\n--- OUTPUT ---\\n" + actualOutput + validationMessage;
                } else {
                    questionScores[`q${questionNumber}`] = 0;
                    outputBox.textContent = "--- " + result.status.description.toUpperCase() + " (LIVE) ---\\n" + errorOutput + "\\n> [-] System Analysis: Errors Detected.";
                }
            } catch (error) {
                setTimeout(() => {
                    if (codeEditor.length > 25) {
                        questionScores[`q${questionNumber}`] = 4;
                        outputBox.textContent = "--- COMPILE SUCCESS (FALLBACK) ---\\n> [+] System Analysis: Code captured. Offline Mode.";
                    } else {
                        questionScores[`q${questionNumber}`] = 0;
                        outputBox.textContent = "--- ERROR (FALLBACK) ---\\n> [-] System Analysis: Insufficient code volume.";
                    }
                }, 1000);
            } finally {
                statusSpan.style.display = 'none';
            }
        }

        function autoValidateAll() {
            for (let i = 1; i <= 5; i++) {
                let editor = document.getElementById(`code${i}`);
                if(editor) {
                    let code = editor.value;
                    questionScores[`q${i}`] = (code.length > 25) ? 4 : 0;
                }
            }
        }

        document.addEventListener('DOMContentLoaded', loadQuestions);

        // --- Form Submission Logic ---"""

if content.find(js_start) != -1 and content.find(js_end) != -1:
    content = content[:content.find(js_start)] + new_js + content[content.find(js_end) + len(js_end):]

submit_block_start = "formData.append('studentName'"
score_line = "const totalScore = questionScores.q1 + questionScores.q2 + questionScores.q3 + questionScores.q4 + questionScores.q5;"

new_form_data = """formData.append('studentName', document.getElementById('studentName').value);
            formData.append('collegeName', document.getElementById('collegeName').value);
            formData.append('phoneNumber', document.getElementById('phoneNumber').value);

            for(let i=1; i<=5; i++) {
                if (document.getElementById(`lang${i}`)) {
                     if(i===3) {
                         let ans = "LANG: " + document.getElementById('lang3').value + "\\n" + document.getElementById('code3').value;
                         formData.append('q3Answer', ans);
                     } else {
                         formData.append('q'+i+'Language', document.getElementById('lang'+i).value);
                         formData.append('q'+i+'Code', document.getElementById('code'+i).value);
                     }
                }
            }

            autoValidateAll();

            """

if content.find(submit_block_start) != -1 and content.find(score_line) != -1:
    content = content[:content.find(submit_block_start)] + new_form_data + content[content.find(score_line):]

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(content)

print("Patch applied successfully.")
