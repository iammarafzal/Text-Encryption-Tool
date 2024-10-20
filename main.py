from tkinter import *
import random
import string

def generate_random_string(length=3):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Encryption Tool")
        self.root.geometry('450x430+100+100')
        self.root.resizable(False, False)


        # --------------------------- Input and Output Labels ---------------------------
        lblTextHere = Label(self.root, text="Enter Text Here:", font=("Arial", 12, "bold"), pady=10)
        lblTextHere.pack(side=TOP, fill=X)
        lblTextHere.place(x=170)

        lblOutputTextHere = Label(self.root, text="Output Text Here:", font=("Arial", 12, "bold"))
        lblOutputTextHere.place(x=160, y=240)


        # --------------------------- DataFrames ---------------------------
        Input_DataFrame = Frame(self.root, bg='white', width=430, height=152)
        Input_DataFrame.place(x=10, y=35)

        Output_DataFrame = Frame(self.root, bg='white', width=430, height=152)
        Output_DataFrame.place(x=10, y=265)


        # --------------------------- Text Boxes ---------------------------
        self.InputTextBox = Text(Input_DataFrame, font=("Arial", 13), bg="white", width=46, height=6)
        self.InputTextBox.place(x=0, y=0)

        self.OutputTextBox = Text(Output_DataFrame, font=("Arial", 13), bg="white", width=46, height=6)
        self.OutputTextBox.place(x=0, y=0)




        # --------------------------- Buttons ---------------------------
        encrypt_btn = Button(self.root, text="Encrypt", font=("Arial", 10, "bold"), width=12, bg="red", fg="white", pady=3, padx=6, command=self.encrypt_func)
        encrypt_btn.place(x=110, y=195)

        decrypt_btn = Button(self.root, text="Decrypt", font=("Arial", 10, "bold"), width=12, bg="green", fg="white", pady=3, padx=6, command=self.decrypt_func)
        decrypt_btn.place(x=250, y=195)

        # Copy Button
        btnCopy = Button(Output_DataFrame, text="Copy", font=("Arial", 9, "bold"), width=8, bg="black", fg="white", command=self.copy_output_text)
        btnCopy.place(x=359, y=121)

        # Paste Button
        btnPaste = Button(Input_DataFrame, text="Paste", font=("Arial", 9, "bold"), width=8, bg="black", fg="white", command=self.paste_to_input)
        btnPaste.place(x=288, y=121)
        
        btnClear_TextBox = Button(Input_DataFrame, text="Clear", font=("Arial", 9, "bold"), width=8, bg="black", fg="white", command=self.clear_textbox)
        btnClear_TextBox.place(x=359, y=121)


        # --------------------------- Scroll Bars ---------------------------
        sc_y = Scrollbar(Input_DataFrame, orient=VERTICAL, command=self.InputTextBox.yview)
        sc_y.place(x=413, y=0, height=120)
        self.InputTextBox.config(yscrollcommand=sc_y.set)

        sc_y = Scrollbar(Output_DataFrame, orient=VERTICAL, command=self.OutputTextBox.yview)
        sc_y.place(x=413, y=0, height=120)
        self.OutputTextBox.config(yscrollcommand=sc_y.set)
    
        
        # --------------------------- Functions ---------------------------


    def clear_textbox(self):
        self.InputTextBox.delete("1.0", END)


    def paste_to_input(self):
        try:
            clipboard_text = self.root.clipboard_get()
            self.InputTextBox.delete("1.0", END)
            self.InputTextBox.insert(END, clipboard_text)
        except Exception as e:
            self.show_error(f"Paste failed: {str(e)}")


    def str_to_words(self):
        text = self.InputTextBox.get("1.0", END).strip()
        return text.split()

    def encrypt_func(self):
        try:
            nwords = []
            words = self.str_to_words()
            for word in words:
                if len(word) >= 3:
                    rr = generate_random_string()
                    strnew = rr + word[1:] + word[0] + rr
                    nwords.append(strnew)
                else:
                    nwords.append(word[::-1])
            encrypted_text = " ".join(nwords)

            self.OutputTextBox.delete("1.0", END)
            self.OutputTextBox.insert(END, encrypted_text)
        except Exception as e:
            self.show_error(f"Encryption failed: {str(e)}")


    def decrypt_func(self):
        try:
            nwords = []
            words = self.str_to_words()
            for word in words:
                if len(word) >= 3:
                    strnew = word[3:-3]
                    strnew = strnew[-1] + strnew[:-1]
                    nwords.append(strnew)
                else:
                    nwords.append(word[::-1])
            decrypted_text = " ".join(nwords)

            self.OutputTextBox.delete("1.0", END)
            self.OutputTextBox.insert(END, decrypted_text)
        except Exception as e:
            self.show_error(f"Decryption failed: {str(e)}")

    def copy_output_text(self):
        try:
            output_text = self.OutputTextBox.get("1.0", END).strip()
            self.root.clipboard_clear()
            self.root.clipboard_append(output_text)
            self.root.update()
        except Exception as e:
            self.show_error(f"Copy failed: {str(e)}")


    def show_error(self, message):
        error_window = Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100+180+250")
        error_window.resizable(False, False)
        
        Label(error_window, text=message, fg="red", font=("Arial", 10)).pack(pady=20)
        Button(error_window, text="OK", command=error_window.destroy).pack()
        

root = Tk()
Window(root)
root.mainloop()
