# ``WKInternalsNotes/WKExtrinsicButton/extrinsicContentSize``

ボタンの `intrinsicContentSize` に反映するサイズを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) CGSize extrinsicContentSize;
```

## Default Value
`CGSizeZero`。

## Discussion
設定時に `_extrinsicContentSize` を更新し、`invalidateIntrinsicContentSize` を呼ぶ。`intrinsicContentSize` はこの値を返す。

## References
- [`WKExtrinsicButton.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.h#L38)
- [`WKExtrinsicButton.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.mm#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
