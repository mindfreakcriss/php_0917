<?php

function find_letter($string1, $string2)
{
    $array = array_fill(0, 26, 0);
    $length = strlen($string2);
    for ($i = 0; $i < $length; $i++) {
        $array[ord($string2[$i]) - ord('a')]++;
    }
    $length2 = strlen($string1);
    for ($j = 0; $j < $length2; $j++) {
        $array[ord($string1[$j]) - ord('a')]--;
        if ($array[ord($string1[$j]) - ord('a')] < 0) {
            return false;
        }
    }
    return true;
}