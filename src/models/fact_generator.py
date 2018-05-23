import random
import os


class FactGenerator(object):
    @staticmethod
    def puppy_fact_generator():
        lines = open('/Users/phillipoliveria/PycharmProjects/puppy_facts/src/puppy_facts.txt').read().splitlines()
        fact = random.choice(lines)
        return fact

    @staticmethod
    def puppy_image_generator():
        img = ""
        file = random.choice(os.listdir("/Users/phillipoliveria/PycharmProjects/puppy_facts/src/insta_urls"))
        lines = open("/Users/phillipoliveria/PycharmProjects/puppy_facts/src/insta_urls/{}".format(file)).read().splitlines()
        while any([(img.endswith('.mp4')), (img == "")]):
            img = random.choice(lines)
        insta_tag = "@" + os.path.basename(file).strip('.txt')
        return img, insta_tag

    @classmethod
    def puppy_fact_attachment(cls):
        img, insta_tag = cls.puppy_image_generator()
        attachment = [
            {
                "fallback": "Puppy Facts.",
                "color": "#36a64f",
                "author_name": insta_tag,
                "image_url": img,
                "ts": 123456789
            }
        ]
        return attachment
