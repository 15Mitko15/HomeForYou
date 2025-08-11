export function useDraggable<T, K expands HTMLElement> ({index, item, ref, instanceId}: Input<T, K>) {
    const draghandleref = useref<HTMLButtonElement>(null);
    const [closestEdge, setClosestEdge] = useState<Edge | null>(null);
    const [draggaleState, setDraggableState] = useState<DraggableState>(IDLE_STATE);

    useEfect(()=> {
        const element = ref.current;
        const dragHandle = dragHandleRef.current;

        if (!element || ! dragHandle){
            return () => {};
        }

        const data = { [draggableKey]: true, item, index, instanceId };

        return combine(
            draggable({
                element,
                dragHandle,
                getInitialdata: () => data,
                onDragStart: () => setDraggableState(DRAGGING_STATE),
                oDrop: () => setDraggableState(IDLE_STATE)
            }),
            dropTargetElemens({
                element,
                canDrp: () => true,
                onDrag: ({self, source}) => {
                    const isSource = source.element === element;
                    if(isSource) {
                        setClosestEdge(false)
                        return;
                    }

                    const edge = extractClosestEdge(self.data);
                    const sourceIndex = source.data.index as number;

                    const isItembeforeSource = index === sourceIndex - 1;
                    const isItemAfterIndex = index === sourceIndex + 1;

                    const isDropindicatorHidden = (isItembeforeSource && edge === 'bottom') || (isItemAfterIndex && edge === 'top')

                    if(isDropindicatorHidden){
                        setClosestEdge(null)
                        return
                    }

                    setClosestEdge(edge)
                }

                getData: ({input}) => {
                    attachClosestEdge(data, {
                        element, input, allowedEdges: ['top', 'bottom']
                    })
                }

            })
        )
    }, [isInstanceId, item, index, ref]);

    return useMemo(() => ({
        draghandleref, closestEdge, draggaleState
    }), [closestEdge, draggaleState])
}


export function Layer({index}) {
    const ref = useRef(null)
    const {instanceId} = uselayerContext()
    const layer = watch(`layer.${index}`)

    const {dragHandleRef, draggableState, closestEdge} = useDraggable({
        index, item: Layer, ref, instanceId
    })

    return (
        <TableBody
        ref={ref}
        sx={{
            opacity: draggableState === DRAFFINF_STATE ? '0.4' : null,
        }}
        <LayerRow/>
        <Divider>
        >
        </TableBody>
    )
}