# ``WKInternalsNotes/_WKTargetedElementRequest/initWithPoint(_:)``

座標を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithPoint:(CGPoint)point;
```

## Discussion
`[self init]` 後に `_request->setPoint` を設定する。

## References
- [`_WKTargetedElementRequest.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.h#L37)
- [`_WKTargetedElementRequest.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
