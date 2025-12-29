# ``WKInternalsNotes/WKImageAnalysisGestureRecognizer/lastTouchedScrollView``

最後にタッチされたスクロールビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIScrollView *lastTouchedScrollView;
```

## Default Value
`touchesBegan:` で検出したスクロールビュー。`reset` で `nil` に戻る。

## Discussion
`scrollViewForTouches` の結果を弱参照で保持する。

## References
- [`WKImageAnalysisGestureRecognizer.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.h#L43)
- [`WKImageAnalysisGestureRecognizer.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
