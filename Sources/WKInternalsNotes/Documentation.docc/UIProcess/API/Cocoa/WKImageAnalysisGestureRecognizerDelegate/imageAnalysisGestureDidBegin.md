# ``WKInternalsNotes/WKImageAnalysisGestureRecognizerDelegate/imageAnalysisGestureDidBegin(_:)``

画像解析ジェスチャ開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)imageAnalysisGestureDidBegin:(WKImageAnalysisGestureRecognizer *)gesture;
```

## Discussion
`WKContentView` 側の実装では Live Text が有効であることを前提に、スクロール中なら何もしない。新しいリクエスト ID を生成して既存の解析をキャンセルし、位置情報取得をトリガーして解析対象の画像条件を満たす場合に解析を開始する。

## References
- [`WKImageAnalysisGestureRecognizer.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.h#L35)
- [`WKContentViewInteraction.mm#L13066`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13066)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
