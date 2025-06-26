import string
import secrets
#  виклик функції та кількість символів
def generate_password(lenght=16):
    # всі групи символів

   alphabet =( string.ascii_lowercase \
            + string.ascii_uppercase \
            + string.digits \
            + string.punctuation
    )
# збірка паролю з випадкових символів
   return ''.join(secrets.choice(alphabet) for _ in range(lenght))

if __name__ =="__main__":
    print("Ваш новий пароль:", generate_password(16))

