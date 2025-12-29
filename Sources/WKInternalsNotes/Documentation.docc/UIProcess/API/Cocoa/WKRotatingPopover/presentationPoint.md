# ``WKInternalsNotes/WKRotatingPopover/presentationPoint``

ポップオーバー表示位置の基準点。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) CGPoint presentationPoint;
```

## Default Value
`CGPointZero`。

## Discussion
`initWithView:` で `CGPointZero` に設定され、`presentPopoverAnimated:` では `CGPointZero` の場合にフォーカス要素の `interactionRect` を使う。

## References
- [`WKFormPopover.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L42)
- [`WKFormPopover.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
