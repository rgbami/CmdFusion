<div align="center">
	
# CmdFusion

#### 💻 the command-line utility that can streamline and simplify complex sequences of commands

</div>

----

#### Dependenices: 
   - You need to have the latest version of python downloaded on your device
   - You can download python from the [offical website](https://www.oracle.com/uk/java/technologies/downloads/) for free

----

#### How to set up: 

1. create a ~/bin/ directory if you don't have one already

2. add the file cmdfusion.py from above into the ~/bin/ directory

3. go to the directory in your terminal and run the following command 
   ```
   chmod +x ~/cmdfusion.py
   ```
   this wil make the python file executable:

5. Add the following .zshrc configurations above to your own .zshrc file, making it easier to call the python file (pls note you can alter the function name here to change the terminal alias if desired)

6. after updating the .zshrc file run the following command to reload your zsh configuration:
   ```
   source ~/.zshrc
   ```

7. Usage in zsh: Now, you can use the cmdfusion command directly in zsh. For example:
    ```
   cmdfusion list_files
    ```


----

#### Here's all the things you can do now: 

- Define Aliases: Users define aliases for their command sequences in a configuration file or via a command-line interface. For example:

  ```
  cmdfusion alias mycmd "echo 'Hello' && ls -l && grep 'test'"
  ```



- Execute Aliases: Users run the defined alias with a single command:
	```
	cmdfusion mycmd
	```


- Parameter Replacement: Aliases can include placeholders for parameters:
	```
	cmdfusion alias mycmd "echo {greeting} && ls {directory}"
	```


- Execution:
	```
	cmdfusion mycmd --greeting "Hello" --directory "/home/user"
	```


- Chain Commands: Support chaining commands with conditionals:
	```
	cmdfusion alias mycmd "mkdir {dir} && cd {dir} && touch file.txt"
	```
