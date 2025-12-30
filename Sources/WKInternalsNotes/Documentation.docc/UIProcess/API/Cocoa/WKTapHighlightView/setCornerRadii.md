# ``WKInternalsNotes/WKTapHighlightView/setCornerRadii(_:)``

矩形の角丸情報を保持する。

## Objective-C Declaration
```objective-c
- (void)setCornerRadii:(WebCore::FloatRoundedRect::Radii&&)radii;
```

## Discussion
`_cornerRadii` に `WTFMove` で代入する。

## References
- [`WKTapHighlightView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.h#L39)
- [`WKTapHighlightView.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
