from functions import *



while (True):


    print("\n1.Encrypt \t 2.Decrypt\n")

    ch = int(input("\nSelect your Choice: "))

    if (ch == 1):
        text = input("\nEnter the text that you want to encrypt:\n")

        encrypt_tp = encrypt(text)


        print("\nYour Encrypted text is {}".format(encrypt_tp[0]))

        print("\nYor Decryption Key is {}".format(encrypt_tp[1]))
        print("Please copy your decryption key as well.")




    elif (ch == 2):

        en_text = input("\nEnter the encrypted text: \n")

        key = input("\nEnter the decryption key: ")

        message = decrypt(en_text,key)

        print("The Decrypted Message is: \n{}\n".format(message))



    else:
        print("\nInvalid Option!!\nEnter again...")



    ex = input("\nDo you want to repeat the program? (y/n)")

    if (ex == 'y'):
        continue

    else:
        break



