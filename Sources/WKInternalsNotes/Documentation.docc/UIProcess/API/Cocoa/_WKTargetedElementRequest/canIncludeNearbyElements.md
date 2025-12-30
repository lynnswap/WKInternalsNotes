# ``WKInternalsNotes/_WKTargetedElementRequest/canIncludeNearbyElements``

近傍要素の含有可否を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL canIncludeNearbyElements;
```

## Default Value
`NO`。

## Discussion
`_request->canIncludeNearbyElements()` の getter/setter を直接委譲する。

## References
- [`_WKTargetedElementRequest.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.h#L41)
- [`_WKTargetedElementRequest.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.mm#L94)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
