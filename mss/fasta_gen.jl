using FastaIO

const seed = "COMMONSUBSTR"
const fastadir = joinpath(@__DIR__, "fastas")
mkpath(fastadir)


function create_dna_sequence(length)
    return join(rand(['A', 'C', 'G', 'T'], length))
end

FastaWriter(joinpath(fastadir, "sample.fa")) do fw
    for i in 1:15
        header = string("seq_", i)
        seq = string(
            create_dna_sequence(rand(5:50)),
            seed,
            create_dna_sequence(rand(5:200))
        )
        writeentry(fw, header, seq)
    end
end

open(joinpath(fastadir, "empty.fa"), "w") do f
    write(f, ">seq_1\n>seq_2\n\n>seq_3")
end

FastaWriter(joinpath(fastadir, "different_lengths.fa")) do fw
    writeentry(fw, "seq_1", "CCGTC$seed")
    writeentry(fw, "seq_2", "GTGCTGTATAC$(seed)CGCTACACACGCAGCAGC")
    writeentry(fw, "seq_3", seed)
end

FastaWriter(joinpath(fastadir, "no_common.fa")) do fw
    writeentry(fw, "seq_1", "ABCDEFG")
    writeentry(fw, "seq_2", "HIJKLMN")
    writeentry(fw, "seq_3", "OPQRSTU")
end

FastaWriter(joinpath(fastadir, "special_characters.fa")) do fw
    writeentry(fw, "seq_1", "^&*(&)$(seed)(*(46574&*^599))")
    writeentry(fw, "seq_2", "8796^*^&^%*&$(seed)^(860)")
    writeentry(fw, "seq_3", "465745907$(seed)6(&_()&^%6785364)")
end

FastaWriter(joinpath(fastadir, "case_sensitivity.fa")) do fw
    writeentry(fw, "seq_1", lowercase(seed))
    writeentry(fw, "seq_2", titlecase(seed))
    writeentry(fw, "seq_3", uppercase(seed))
end

FastaWriter(joinpath(fastadir, "identical_strings.fa")) do fw
    for i in 1:3
        writeentry(fw, "seq_$i", seed)
    end
end

FastaWriter(joinpath(fastadir, "large_input.fa")) do fw
    for i in 1:10
        create_dna_sequence(rand(1000:2000))
        seq = create_dna_sequence(rand(1000:2000)) * seed * create_dna_sequence(rand(1000:2000))
        writeentry(fw, "seq_$i", seq)
    end
end