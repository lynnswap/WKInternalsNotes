# ``WKInternalsNotes/_WKTargetedElementRequest/shouldIgnorePointerEventsNone``

`pointer-events: none` を無視するかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldIgnorePointerEventsNone;
```

## Default Value
`NO`。

## Discussion
`_request->shouldIgnorePointerEventsNone()` の getter/setter を直接委譲する。

## References
- [`_WKTargetedElementRequest.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.h#L42)
- [`_WKTargetedElementRequest.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.mm#L104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
