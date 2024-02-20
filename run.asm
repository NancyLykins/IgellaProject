section .data
    prog db "/usr/bin/python", 0 ; program to execute
    arg1 db "python", 0 ; argv[0]
    arg2 db "bot/client.py", 0 ; argv[1]
    argv dq arg1, arg2, 0 ; argument vector
    envp dq 0 ; environment pointer

section .text
    global _start

_start:
    ; prepare the arguments for execve
    mov rax, 59 ; syscall number for execve
    mov rdi, prog ; first argument: program path
    mov rsi, argv ; second argument: arguments array
    mov rdx, envp ; third argument: environment array

    int 0x80
