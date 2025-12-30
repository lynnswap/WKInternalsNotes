# ``WKInternalsNotes/WKUIScrollEdgeEffect/usesHardStyle``

`UIScrollEdgeEffectStyle.hardStyle` を使用しているかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL usesHardStyle;
```

## Default Value
初期値は `NO`（`setStyle:` で更新）。

## Discussion
`setStyle:` で `style` が `hardStyle` かどうかを判定して `_usesHardStyle` を更新し、上辺のエフェクトで値が変化した場合に `WKScrollView` へ通知する。

## References
- [`WKUIScrollEdgeEffect.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.h#L42)
- [`WKUIScrollEdgeEffect.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
