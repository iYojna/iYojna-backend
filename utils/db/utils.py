from butter_knife.main import get_all_schemes

from schemes.serializers import EnglishSchemeModelSerializer, GujSchemeModelSerializer
from googletrans import Translator

from user.models import User
from user.serializers import RegisterSerializer

translator = Translator()


def update_schemes():
    schemes = get_all_schemes()
    for scheme in schemes:
        en_serializer = EnglishSchemeModelSerializer(data=scheme["en"])
        gu_serializer = GujSchemeModelSerializer(data=scheme["gu"])

        en_valid = en_serializer.is_valid()
        gu_valid = gu_serializer.is_valid()
        if en_valid and gu_valid:
            en_serializer.save()
            gu_serializer.save()
        else:
            print(en_serializer.errors)
            print(gu_serializer.errors)

        print(scheme["en"]["name"])


def is_eligible(scheme: EnglishSchemeModelSerializer.data, user):
    return True
    user = User.objects.get(username="+919174400406")
    # user = RegisterSerializer(user).data
    # if not user.is_authenticated:
    #     return False

    if scheme.get("max_inc") and user.get("income"):
        if user.get("income") > scheme.get("max_inc"):
            return False
    if scheme.get("min_inc") and user.get("income"):
        if user.get("income") < scheme.get("min_inc"):
            return False
    if scheme.get("min_age") and user.age:
        print(user.age, scheme.get("min_age"))
        if user.age < scheme.get("min_age"):
            return False
    if scheme.get("max_age") and user.age:
        if user.age > scheme.get("max_age"):
            return False
    if scheme.get("educational_qualifications") and user.get("education"):
        if user.get("education") < scheme.get("educational_qualifications"):
            return False
    return True


def generate_gu_db(english_objects):
    ...


if __name__ == '__main__':
    update_schemes()
