#!/usr/bin/perl
no warnings qw(uninitialized void); # deactive noisy warnings
# http://users.skynet.be/chricat/ChiffresLettres.html

$WORDLIST = "<wordlist.txt";
open WORDLIST or die "can't open $WORDLIST\n";
%ANAGRAM = ();
while (my $line = <WORDLIST>){
	chomp $line;
	$line =~ s/\r//g; # get rif of Windows crlf
	$sorted = join("", sort split("", $line));
	$ANAGRAM{$sorted} = "$line,$ANAGRAM{$sorted}"; # the key is the sorted anagram of the word
}

# print scalar keys %ANAGRAM;
# 307997

if ($ARGV[0]){ 
	doit($ARGV[0]); }
else {
	$| = 1; # always flush stdout 
	for (;;){
		print "\nLettres: "; 
		if ($line = <STDIN>){
			chomp $line; 
			doit($line); 
		} else {
			exit(0); 
		}
	}
}

sub bylength {
	my @A = split ',', $a;
	my @B = split ',', $b;
	# $x <=> $y returns 
	# -1 :  $x is lesser than $y
	#  0 : $x equal to  $y
	#  1 : if $x is greater than $y
	return(length($A[0]) <=> length($B[0])); 
}

sub doit {
	my ($x) = @_; 
	my %SOLUTION;

	my @GIVEN = sort split("", uc($x));
	for ($i = 0; $i < 32768; $i++){ # each letter is taken or not (binary, one bit per letter)
		my $candidat = ""; # initialize !
		for ($bit = 0; $bit < 15; $bit++){
			if ($i & (1 << $bit)){
				$candidat = "$candidat"."$GIVEN[$bit]";
			}
		}
		my $soluce = "";
		if ($soluce = $ANAGRAM{$candidat}){ # if this anagram exists, take note
			print "$ANAGRAM{$candidat}\n";
			$SOLUTION{$soluce} = length $soluce;
		}
	}
	
	print "-------------------------\nAnagrammes de [" . uc($x) . " - " . length($x) . "]\n-------------------------\n";
	foreach $key (sort bylength keys %SOLUTION){ # print solutions sorted by length
		my @C = split ',',$key;
		print "[" . length( $C[0]) . "] $key\n";
	}
}
