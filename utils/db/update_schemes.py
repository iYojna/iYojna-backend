from butter_knife.main import get_all_schemes
from schemes.serializers import EnglishSchemeModelSerializer, GujSchemeModelSerializer


def main():
    schemes = get_all_schemes()
    for scheme in schemes:
        en_serializer = EnglishSchemeModelSerializer(data=scheme["en"])
        gu_serializer = GujSchemeModelSerializer(data=scheme["gu"])

        if en_serializer.is_valid() and gu_serializer.is_valid():
            en_serializer.save()
            gu_serializer.save()
        else:
            print(en_serializer.errors)
            print(gu_serializer.errors)
            break


if __name__ == '__main__':
    main()
