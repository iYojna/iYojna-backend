from butter_knife.main import get_all_schemes
from schemes.serializers import EnglishSchemeModelSerializer, GujSchemeModelSerializer


def main():
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


if __name__ == '__main__':
    main()
