<?php

$array = [3,17,75,80,202];

/**
 * @Description: Searches for a target value in a sorted array and returns its index or -1 if not found.
 *
 * @param $array
 * @param $target
 * @return int|string
 */
function search($array, $target) {
    foreach ($array as $index => $value) {
        if ($value === $target) {
            return $index;
        } else if ($value > $target) {
            break; // Stop searching if the current value exceeds the target
        }
    }
    return -1; // Target not found
}

/**
 * @Description: Performs a binary search on a sorted array to find the index of the target value.
 *
 * @param $array
 * @param $target
 * @return int
 */
function binary_search($array, $target)
{
    $left = 0;
    $right = count($array) - 1;

    while ($left <= $right) {
        $mid = intdiv($left + $right, 2);

        if ($array[$mid] === $target) {
            return $mid; // Target found
        } elseif ($array[$mid] < $target) {
            $left = $mid + 1; // Search in the right half
        } else {
            $right = $mid - 1; // Search in the left half
        }
    }

    return -1; // Target not found
}

function bubble_sort($array)
{
    $length = count($array);

    for ($i = 0; $i < $length; $i ++) {
        for ($j = $i + 1; $j < $length; $j++) {
            if ($array[$i] > $array[$j]) {
                // Swap
                $temp = $array[$i];
                $array[$i] = $array[$j];
                $array[$j] = $temp;
            }
            var_dump($array);
        }
    }
    return $array;
}

/**
 * @Description 选择排序, 比冒泡排序少了一些交换
 *
 * @param $array
 * @return mixed
 */
function select_sort($array)
{
    $length = count($array);
    for ($i = 0; $i < $length; $i++) {
        $begin = $i;
        for ($j = $i + 1; $j < $length; $j++) {
            if ($array[$begin] > $array[$j]) {
                $begin = $j;
            }
        }
        if ($i != $j) {
            $temp = $array[$i];
            $array[$i] = $array[$begin];
            $array[$begin] = $temp;
        }
    }
    return $array;
}

$array = [ 1, 4, 3,2];

var_dump(select_sort($array));