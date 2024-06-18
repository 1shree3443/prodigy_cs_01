{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7162a2f5",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 13)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m<tokenize>:13\u001b[1;36m\u001b[0m\n\u001b[1;33m    return result\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "#A python program to illustrate Caesar Cipher Technique\n",
    "def encrypt(text,s):\n",
    "\tresult = \"\"\n",
    "\tfor i in range(len(text)):\n",
    "\t\tchar = text[i]\n",
    "if (char.isupper()):\n",
    "            result += chr((ord(char) + s-65) % 26 + 65)\n",
    "\n",
    "\t\t# Encrypt lowercase characters\n",
    "\t\telse:\n",
    "\t\t\tresult += chr((ord(char) + s - 97) % 26 + 97)\n",
    "\n",
    "\treturn result\n",
    "\n",
    "#check the above function\n",
    "text = \"ATTACKATONCE\"\n",
    "s = 4\n",
    "print (\"Text : \" + text)\n",
    "print (\"Shift : \" + str(s))\n",
    "print (\"Cipher: \" + encrypt(text,s))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "002f0693",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter text:aaaa\n",
      "shift value:4\n",
      "Text : aaaa\n",
      "Shift : 4\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 24\u001b[0m\n\u001b[0;32m     22\u001b[0m \u001b[38;5;28mprint\u001b[39m (\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mText : \u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m+\u001b[39m text)\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28mprint\u001b[39m (\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mShift : \u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m+\u001b[39m (s))\n\u001b[1;32m---> 24\u001b[0m \u001b[38;5;28mprint\u001b[39m (\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCipher: \u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m+\u001b[39m encrypt(text,s))\n",
      "Cell \u001b[1;32mIn[6], line 15\u001b[0m, in \u001b[0;36mencrypt\u001b[1;34m(text, s)\u001b[0m\n\u001b[0;32m     11\u001b[0m \t\tresult \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;28mchr\u001b[39m((\u001b[38;5;28mord\u001b[39m(char) \u001b[38;5;241m+\u001b[39m s\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m65\u001b[39m) \u001b[38;5;241m%\u001b[39m \u001b[38;5;241m26\u001b[39m \u001b[38;5;241m+\u001b[39m \u001b[38;5;241m65\u001b[39m)\n\u001b[0;32m     13\u001b[0m \t\u001b[38;5;66;03m# Encrypt lowercase characters\u001b[39;00m\n\u001b[0;32m     14\u001b[0m \t\u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m---> 15\u001b[0m \t\tresult \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;28mchr\u001b[39m((\u001b[38;5;28mord\u001b[39m(char) \u001b[38;5;241m+\u001b[39m s \u001b[38;5;241m-\u001b[39m \u001b[38;5;241m97\u001b[39m) \u001b[38;5;241m%\u001b[39m \u001b[38;5;241m26\u001b[39m \u001b[38;5;241m+\u001b[39m \u001b[38;5;241m97\u001b[39m)\n\u001b[0;32m     17\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6efe2e18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-------------------------------------------- Caesar Cipher Tool --------------------------------------------------\n",
      "\n",
      "Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: shree\n",
      "Invalid action. Please choose 'e', 'd', or 'q' to quit.\n",
      "Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: e\n",
      "Enter the message (invisible, type carefully): ········\n",
      "Please check whether the message you provided was correct or not using the following hints:\n",
      "\n",
      "First and last characters of the message: s***e\n",
      "Total number of characters entered: 5\n",
      "Number of alphabetical letters: 5\n",
      "Number of digits: 0\n",
      "No special characters in the message.\n"
     ]
    }
   ],
   "source": [
    "import getpass\n",
    "\n",
    "print(\"-------------------------------------------- Caesar Cipher Tool --------------------------------------------------\")\n",
    "print(\"\")\n",
    "\n",
    "def analyze_message(message):\n",
    "    num_letters = sum(c.isalpha() for c in message)\n",
    "    num_digits = sum(c.isdigit() for c in message)\n",
    "    num_special = len(message) - num_letters - num_digits\n",
    "\n",
    "    print(f\"Please check whether the message you provided was correct or not using the following hints:\")\n",
    "    print(f\"\\nFirst and last characters of the message: {message[:1]}***{message[-1]}\")\n",
    "    print(f\"Total number of characters entered: {len(message)}\")\n",
    "    print(f\"Number of alphabetical letters: {num_letters}\")\n",
    "    print(f\"Number of digits: {num_digits}\")\n",
    "    \n",
    "    if num_special > 0:\n",
    "        print(f\"Number of special characters: {num_special}\")\n",
    "        print(\"Special characters are present in the message.\")\n",
    "    else:\n",
    "        print(\"No special characters in the message.\")\n",
    "\n",
    "def caesar_cipher(text, shift, action):\n",
    "    result = \"\"\n",
    "    for char in text:\n",
    "        if char.isalpha():\n",
    "            start = ord('a') if char.islower() else ord('A')\n",
    "            if action == 'e':\n",
    "                result_char = chr((ord(char) - start + shift) % 26 + start)\n",
    "            elif action == 'd':\n",
    "                result_char = chr((ord(char) - start - shift) % 26 + start)\n",
    "            else:\n",
    "                raise ValueError(\"Invalid action. Use 'e' to encrypt or 'd' to decrypt\")\n",
    "            result += result_char\n",
    "        else:\n",
    "            result += char\n",
    "    return result\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        action = input(\"Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: \").lower()\n",
    "        if action == 'q':\n",
    "            print(\"Exiting the program. Goodbye!\")\n",
    "            return\n",
    "        elif action in ['e', 'd']:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid action. Please choose 'e', 'd', or 'q' to quit.\")\n",
    "\n",
    "    if action == 'q':\n",
    "        return\n",
    "\n",
    "    \n",
    "    message = getpass.getpass(prompt=\"Enter the message (invisible, type carefully): \")\n",
    "\n",
    "    if action != 'q':\n",
    "        analyze_message(message)\n",
    "\n",
    "        \n",
    "        shift = int(getpass.getpass(prompt=\"Enter the shift value (invisible, type carefully): \"))\n",
    "\n",
    "        if action == 'e':\n",
    "            result = caesar_cipher(message, shift, 'e')\n",
    "            print(\"\\nEncrypted Message:\", result)\n",
    "        elif action == 'd':\n",
    "            result = caesar_cipher(message, shift, 'd')\n",
    "            print(\"\\nDecrypted Message:\", result)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03728b51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
