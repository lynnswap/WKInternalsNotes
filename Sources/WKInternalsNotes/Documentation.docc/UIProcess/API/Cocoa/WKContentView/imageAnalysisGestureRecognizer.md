# ``WKInternalsNotes/WKContentView/imageAnalysisGestureRecognizer``

画像解析用のジェスチャ認識器を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIGestureRecognizer *imageAnalysisGestureRecognizer;
```

## Default Value
`ENABLE(IMAGE_ANALYSIS)` のとき `_imageAnalysisGestureRecognizer` を返し、それ以外は `nil`。

## Discussion
画像解析が有効なビルドでは `_imageAnalysisGestureRecognizer` を返し、無効な場合は `nil` を返す。

## References
- [`WKContentViewInteraction.h#L657`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L657)
- [`WKContentViewInteraction.mm#L2615`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2615)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
