# ``WKInternalsNotes/WKImageAnalysisGestureRecognizer/initWithImageAnalysisGestureDelegate(_:)``

画像解析ジェスチャのデリゲートを設定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithImageAnalysisGestureDelegate:(UIView <WKImageAnalysisGestureRecognizerDelegate> *)delegate;
```

## Discussion
デリゲートを保持し、`minimumPressDuration` や `allowableMovement` を設定して `Image analysis` の名前を付与する。

## References
- [`WKImageAnalysisGestureRecognizer.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.h#L41)
- [`WKImageAnalysisGestureRecognizer.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.mm#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
