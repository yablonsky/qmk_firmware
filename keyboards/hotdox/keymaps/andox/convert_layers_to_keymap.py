import json
import sys


def main(layers_file, output_file=None):
    layers = json.load(open(layers_file))['layers']
    layers = (', '.join(layer) for layer in layers)
    layers = ',\n'.join(f'    [{i}] = LAYOUT_ergodox({layer})' for i, layer in enumerate(layers))
    output = '\n'.join([
        '#include QMK_KEYBOARD_H',
        '',
        'const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {',
        f'{layers}',
        '};'
    ])

    if output_file:
        with(open(output_file, 'w')) as writer:
            writer.write(output)
            print(f' Wrote to file: {output_file} '.center(80, '='))

    return output

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
