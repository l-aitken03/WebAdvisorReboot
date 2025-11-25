# Documentation of Database Elements

## Courses:
*Courses* can be assigned to multiple users, with their participation being dependent on their **role** (determined through linking tables). *Courses* have sections that represent individual offerings of various courses, e.g. two sections meeting at the same time but with two different professors, in person and online sections of the same course, etc. Thus, the *courses* table is the only non-linking table to have a composite primary key (`course_id` AND `section_id`). Most of the columns are self-explanatory, but I will note that the `enroll_status` column is meant to hold values of `OPEN`, `WAITLISTED`, or `CLOSED` to indicate whether students viewing the section offerings for a given semester can enroll in the course or not. (Currently it holds an `INT` value that will be translated via code.)

| Course ID | Section ID | Title      | Dept. | Campus | Term  | Days Offered       | Times         | Enroll Status | Credits |
| --------- | ---------- | ---------- | ----- | ------ | ----- | ------------------ | ------------- | ------------- | ------- |
| MATH-15   | E7294      | Statistics | Math  | Eureka | 2025F | Monday / Wednesday | 10:00 - 12:30 | OPEN          | 4.0     |

## Users:
Fairly self-explanatory. See **Roles** and beyond for more relevant details. 
*Users* will have the following attributes:

| User ID | Username | First Name | Last Name | Email             | Is Professor | Is Student |
| ------- | -------- | ---------- | --------- | ----------------- | ------------ | ---------- |
| 200123  | jdoe123  | JOHN       | DOE       | jdoe123@email.com | No `[0]`     | Yes `[1]`  |
|         |          |            |           |                   |              |            |

## Roles:
*Roles* are broad containers for **Users** that fit into certain categories. *Roles* are associated with **Permissions**, **Operations**, and **Components**. *Roles* will have the following attributes:

| Role ID | Role Name     |
| ------- | ------------- |
| 100     | Guest         |
| 200     | Student       |
| 500     | Professor     |
| 600     | Advisor       |
| 700     | Administrator |

## Permissions:
*Permissions* are explicit individual definitions of what **Operations** a **User** is allowed to perform and/or what **Components** a **User** is allowed to interact with and view. *Permissions* are usually inherited by **Roles** of higher ranking. Therefore, an Advisor would probably have the same *Permissions* for a Professor, Student, and Guest without the restrictions of the lower roles. **Operations** and **Components** are crucially tied to **Roles** and *Permissions*.

| Permission Name       | Permission ID | Associated Role |
| --------------------- | ------------- | --------------- |
| VIEW_CLASS            | 100           | Guest           |
| VIEW_ACCOUNT_SELF     | 200           | Student         |
| EDIT_ACCOUNT_SELF     | 201           | Student         |
| REGISTER_CLASS_SELF   | 212           | Student         |
| DROP_CLASS_SELF       | 213           | Student         |
| VIEW_PLAN             | 220           | Student         |
| EDIT_PLAN             | 221           | Student         |
| REQUEST_CHANGE        | 572           | Professor       |
| VIEW_ACCOUNT_OTHER    | 600           | Advisor         |
| EDIT_ACCOUNT_OTHER    | 601           | Advisor         |
| REMOVE_PLAN           | 623           | Advisor         |
| APPROVE_PLAN          | 626           | Advisor         |
| EDIT_ACCOUNT_ADVANCED | 701           | Administrator   |
| CREATE_ACCOUNT        | 704           | Administrator   |
| DELETE_ACCOUNT        | 705           | Administrator   |
| EDIT_CLASS            | 711           | Administrator   |
| REGISTER_CLASS_OTHER  | 712           | Administrator   |
| DROP_CLASS_OTHER      | 713           | Administrator   |
| APPROVE_CHANGE        | 776           | Administrator   |

| Index | Function           |
| ----- | ------------------ |
| `XX0` | `VIEW`             |
| `XX1` | `EDIT`             |
| `XX2` | `REGISTER/REQUEST` |
| `XX3` | `DROP/REMOVE`      |
| `XX4` | `CREATE`           |
| `XX5` | `DELETE`           |
| `XX6` | `APPROVE`          |
| `X0X` | `ACCOUNT`          |
| `X1X` | `CLASS`            |
| `X2X` | `PLANNING`         |
| `X7X` | `MANAGEMENT`       |
| `1XX` | `GUEST`            |
| `2XX` | `STUDENT`          |
| `5XX` | `PROFESSOR`        |
| `6XX` | `ADVISOR`          |
| `7XX` | `ADMIN`            |


## Operations and Components: (In Progress)
*Operations* are actions that can be taken by a user. *Operations* rely on authentication / general checks with **Roles** and **Permissions** to be successfully completed. 
*Components* are elements/aspects of the application that can be viewed by a user. *Components* rely on authentication / general checks with **Roles** and **Permissions** to make *Operations* accessible to the current user. *Components* are essentially a "view"; student view, faculty view, admin view, etc.

In other words, a **User** must have a **Role**, which by default will be associated with appropriate **Permissions**, to view specific *Components* that are required to perform *Operations*. However, certain roles do not require certain **Permissions** or *Operations*, which will be reflected in the resultant *Component* policy enforced by the linking tables between the **Role**, **Permission**, *Operation*, and *Component* tables.

A student (RID 200) should be able to view their own account (PID 200), edit limited aspects for their own account (PID 201), and register themselves for classes (PID 212), but they should not be able view other user accounts (PID 600), modify advanced information for their profile/account (PID 701), or drop another student from a class (PID 713). At the same time, an administrator (RID 700) doesn't really need to be able to view their own academic plan (PID 220), but they absolutely should be able to approve a change to a course that a professor has requested (PID 776). You can probably notice by the Role ID (RID) and Permission ID (PID) that certain *Components* and **Operations** will naturally be limited to users that are assigned to positions with more advanced duties. 

I need help understanding how to translate operable actions into operation routes and operation types as well as translating component views into component names and component types.

| Operation ID | Operation Route | Operation Type |
| ------------ | --------------- | -------------- |
|              |                 |                |

| Component ID | Component Name | Component Type |
| ------------ | -------------- | -------------- |
|              |                |                |
