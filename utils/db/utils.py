from butter_knife.main import get_all_schemes
from schemes.serializers import EnglishSchemeModelSerializer, GujSchemeModelSerializer


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
    if scheme.max_inc:
        if user.income > scheme.max_inc:
            return False
    if scheme.min_age:
        if user.age < scheme.min_age:
            return False
    if scheme.max_age:
        if user.age > scheme.max_age:
            return False
    if scheme.educational_qualifications:
        if user.education < scheme.educational_qualifications:
            return False

    return True


if __name__ == '__main__':
    update_schemes()
