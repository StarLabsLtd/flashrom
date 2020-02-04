#include <ftdi.h>
struct ftdi_context *ftdic = NULL;
int main(int argc, char **argv)
{
	(void) argc;
	(void) argv;
	return ftdi_init(ftdic);
}
