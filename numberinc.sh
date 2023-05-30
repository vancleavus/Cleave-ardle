#!/bin/bash
awk '$0++' /usr/local/Cleaveardle/number.txt > /usr/local/Cleaveardle/number2.txt && mv /usr/local/Cleaveardle/number2.txt /usr/local/Cleaveardle/number.txt
