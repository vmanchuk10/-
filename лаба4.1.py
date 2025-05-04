from Bio import SeqIO

# вариант 1


def calculate_gc_content(sequence):
    """Вычисляет GC-состав последовательности."""
    gc_count = sequence.upper().count("G") + sequence.upper().count("C")
    return gc_count / len(sequence) * 100


# Задание 2: GC-состав
def analyze_gc_content(genbank_file):
    """Анализирует GC-состав записей в GenBank файле и выводит отсортированный список."""
    records = []
    for record in SeqIO.parse(genbank_file, "genbank"):
        gc_content = calculate_gc_content(record.seq)
        records.append((record.id, gc_content, record.seq))
    records.sort(key=lambda x: x[1])
    print("Записи, отсортированные по возрастанию GC-состава:")
    for record_id, gc_content, _ in records:
        print(f"{record_id}: GC-состав = {gc_content:.2f}%")
    return records


# Задание 3: Трансляция
def analyze_translations(genbank_file):
    """Анализирует трансляции в GenBank файле и выводит информацию о CDS и аминокислотных последовательностях."""
    records_with_translations = []
    for record in SeqIO.parse(genbank_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS" and "translation" in feature.qualifiers:
                coding_sequence_location = feature.location
                translation = feature.qualifiers["translation"][0]
                records_with_translations.append(
                    (record.id, coding_sequence_location, translation)
                )

    print("\nЗаписи с трансляциями:")
    for record_id, coding_sequence_location, translation in records_with_translations:
        print(f"ID записи: {record_id}")
        print(f"Coding sequence location: {coding_sequence_location}")
        print(f"Translation: {translation}")


if __name__ == "__main__":
    genbank_file = "Paralichthys_dentatus_combined.gb"
    gc_results = analyze_gc_content(genbank_file)
    analyze_translations(genbank_file)
