# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlIoCompress(PerlPackage):
    """A perl library for uncompressing gzip, zip, bzip2
    or lzop file/buffer."""

    homepage = "http://search.cpan.org/~pmqs/IO-Compress-2.070/lib/IO/Uncompress/AnyUncompress.pm"
    url      = "http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/IO-Compress-2.081.tar.gz"

    version('2.081', '379932c1b9428b873ed7ad3c1db15872')

    depends_on('perl-compress-raw-zlib', type='run')
    depends_on('perl-compress-raw-bzip2', type='run')
