# Technical Interview & Data Structures Practice Repository

This repository highlights problem sets from my role as a Tech Fellow for CodePath’s Technical Interview Prep 2 course.

The primary objective of this course is to help students:
* Identify Optimal Approaches: Recognize key patterns, algorithms, and data structures suited for complex technical challenges.
* Master Technical Communication: Practice verbalizing their thought processes using the UMPIRE method (Understand, Match, Plan, Implement, Review, Evaluate), placing heavy emphasis on problem comprehension and planning before writing code.

To prepare for weekly mentoring and solution walkthroughs, I solved 3–5 problems per problem set, which are documented across the unit folders in this repository.

---

## 📁 Repository Structure Overview

```text
.
├── README.md
├── upi_template.py
├── unit8_example
├── Unit 1: Foundations/
├── Unit 2: Dictionaries & Sets/
├── Unit 3: Stacks & Queues/
├── Unit 4: OOP & Linked Lists I/
├── Unit 5: Linked Lists II/
├── Unit 7: Recursion/
├── Unit 9/ (Trees & Hierarchical Structures)
└── Unit 10: Graphs/
```

---

## 💡 Skills & Core Concepts by Unit

### **Unit 1: Foundations**
* **Core Topics**: Array Manipulation, String Parsing, Two-Pointer Techniques, Linear Search.
* **Skills Displayed**:
  * Implementing custom iterative searches without built-in library functions.
  * In-place array modifications and bound checking.
  * String filtering, case-insensitive matching, and substring replacement.
  * Handling edge cases in numerical ranges and array gaps.

### **Unit 2: Dictionaries & Sets**
* **Core Topics**: Hash Maps (Dictionaries), Hash Sets, Frequency Counting, Key-Value Lookups.
* **Skills Displayed**:
  * Utilizing $\mathcal{O}(1)$ average-time lookup operations for efficient problem solving.
  * Counting frequency distributions of characters, elements, and sub-sequences.
  * Set operations (intersections, unions, and duplicate removal).
  * Mapping relationships and optimizing nested iterations into linear-time pass solutions.

### **Unit 3: Stacks & Queues**
* **Core Topics**: LIFO (Last-In-First-Out) and FIFO (First-In-First-Out) Principles, Double-ended Queues (`collections.deque`).
* **Skills Displayed**:
  * Parentheses matching, syntax parsing, and stack-based backtracking.
  * Evaluating postfix and infix mathematical expressions.
  * Queue-based scheduling and buffer processing.
  * Monotonic stack/queue techniques for range query problems.

### **Unit 4: OOP & Linked Lists I**
* **Core Topics**: Object-Oriented Programming (OOP), Classes, Instances, Singly Linked Lists.
* **Skills Displayed**:
  * Class definitions, state management, initialization (`__init__`), and encapsulation.
  * Building custom `Node` and `LinkedList` data structure classes.
  * Pointer manipulation: Traversal, Insertion at Head/Tail, and Searching in Linked Lists.
  * Node deletion and memory references management.

### **Unit 5: Linked Lists II**
* **Core Topics**: Advanced Linked List Operations, Two-Pointer Patterns, Fast/Slow Pointers.
* **Skills Displayed**:
  * Reversing a linked list iteratively and recursively.
  * Detecting cycles (Floyd's Cycle Detection / Tortoise and Hare algorithm).
  * Finding the midpoint or $k$-th node from the end of a list.
  * Merging sorted lists and reordering list structures in-place.

### **Unit 7: Recursion**
* **Core Topics**: Call Stack, Base Cases, Recursive Decomposition, Divide and Conquer.
* **Skills Displayed**:
  * Identifying base cases and recursive steps to avoid stack overflow.
  * Converting iterative algorithms into pure recursive function signatures.
  * Permutation and combination generation via decision trees.
  * Mathematical recursion (Factorials, Fibonacci sequence, Exponentiation).

### **Unit 8 & Unit 9: Trees & Binary Search Trees (BST)**
* **Core Topics**: Tree Traversals (In-order, Pre-order, Post-order, Level-order), BST Invariants, Binary Trees.
* **Skills Displayed**:
  * Breadth-First Search (BFS) using Queues and Depth-First Search (DFS) using Stacks/Recursion.
  * Insertion, deletion, and searching within Binary Search Trees ($\mathcal{O}(\log n)$ runtime).
  * Calculating tree parameters: Max depth, balance factor, ancestor paths, and symmetry.

### **Unit 10: Graphs**
* **Core Topics**: Adjacency Lists, Adjacency Matrices, Graph Traversals, Connectivity.
* **Skills Displayed**:
  * Graph representation and building adjacency maps from edge lists.
  * Traversal algorithms: DFS and BFS on directed/undirected graphs.
  * Cycle detection in graphs and identifying connected components.
  * Pathfinding and topological sorting basics.

---

## 🛠️ General Problem-Solving Methodology

Problems in this repository follow the **UPI (Understand, Plan, Implement)** methodology outlined in `upi_template.py`:

1. **Understand**: Clarify inputs, outputs, constraints, and edge cases.
2. **Plan**: Formulate algorithms using pseudocode, diagrams, and time/space complexity estimations ($\mathcal{O}(N)$ analysis).
3. **Implement**: Code clean, modular Python solutions with informative variable names and clear function signatures.

---

## 🚀 How to Use

1. **Prerequisites**: Python 3.x installed.
2. **Execution**: Run individual session files directly via terminal:
   ```bash
   python3 "Unit 1: Foundations/Sess1_Advanced_Ver1.py"
   ```
