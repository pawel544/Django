 function toggleFilters() {

            const panel = document.getElementById('filterPanel');

            const button = document.getElementById('toggleFilters');

            panel.classList.toggle('active');

            const isOpen = panel.classList.contains('active');

            button.textContent = isOpen
                ? 'Ukryj filtry ▲'
                : 'Pokaż filtry ▼';

            button.setAttribute('aria-expanded', isOpen);

        }


        /* KEEP INPUT RANGES CONSISTENT */

        function syncRange(
            fromId,
            toId,
            fromOutputId,
            toOutputId
        ) {

            const from = document.getElementById(fromId);

            const to = document.getElementById(toId);

            if (!from || !to) return;

            const min = Number(
                from.getAttribute('min') || 0
            );

            const max = Number(
                to.getAttribute('max') ||
                from.getAttribute('max') ||
                0
            );

            let fromValue = Number(from.value);

            let toValue = Number(to.value);

            if (!Number.isFinite(fromValue)) {
                fromValue = min;
            }

            if (!Number.isFinite(toValue)) {
                toValue = max;
            }

            fromValue = Math.min(
                Math.max(fromValue, min),
                max
            );

            toValue = Math.min(
                Math.max(toValue, min),
                max
            );

            if (fromValue > toValue) {

                if (document.activeElement === from) {

                    toValue = fromValue;

                } else {

                    fromValue = toValue;

                }

            }

            from.value = fromValue;

            to.value = toValue;

            from.max = toValue;

            to.min = fromValue;

            const fromOutput =
                document.getElementById(fromOutputId);

            const toOutput =
                document.getElementById(toOutputId);

            if (fromOutput) {
                fromOutput.value = fromValue;
            }

            if (toOutput) {
                toOutput.value = toValue;
            }

        }




        function checkCodeRange() {

            syncRange(
                'code_from',
                'code_to',
                'code_from_output',
                'code_to_output'
            );

        }


        /* CHECK TAX RANGE */

        function checkTaxRange() {

            syncRange(
                'tax_number_from',
                'tax_number_to',
                'tax_number_from_output',
                'tax_number_to_output'
            );

        }




        document.addEventListener(
            'DOMContentLoaded',
            function() {

                checkCodeRange();

                checkTaxRange();

            }
        );