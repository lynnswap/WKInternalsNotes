# ``WKInternalsNotes/WKFullscreenStackView/addArrangedSubview(_:applyingMaterialStyle:tintEffectStyle:)``

背景マテリアル設定付きでスタックにサブビューを追加する。

## Objective-C Declaration
```objective-c
- (void)addArrangedSubview:(UIView *)subview applyingMaterialStyle:(AVBackgroundViewMaterialStyle)materialStyle tintEffectStyle:(AVBackgroundViewTintEffectStyle)tintEffectStyle;
```

## Discussion
`AVBackgroundView` に `materialStyle` と `tintEffectStyle` を指定して追加した後、通常の `addArrangedSubview:` も行う（Apple TV 以外）。

## References
- [`WKFullscreenStackView.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullscreenStackView.h#L35)
- [`WKFullscreenStackView.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullscreenStackView.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
