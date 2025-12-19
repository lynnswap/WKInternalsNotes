# ``WKInternalsNotes/WKContentView/_allowAnimationControls()``

アクセシビリティ用のアニメーション制御を許可するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_allowAnimationControls;
```

## Discussion
`ENABLE(ACCESSIBILITY_ANIMATION_CONTROL)` のとき、`self.webView._allowAnimationControls` の値を返す。

## References
- [WKContentViewInteraction.h#L1051](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1051)
- [WKContentViewInteraction.mm#L14677](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14677)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
