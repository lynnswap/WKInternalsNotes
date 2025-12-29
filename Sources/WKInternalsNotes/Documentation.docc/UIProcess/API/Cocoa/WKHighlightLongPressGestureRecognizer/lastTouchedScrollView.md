# ``WKInternalsNotes/WKHighlightLongPressGestureRecognizer/lastTouchedScrollView``

最後にタッチされたスクロールビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) UIScrollView *lastTouchedScrollView;
```

## Default Value
`touchesBegan:` で検出できたスクロールビュー。`reset` で `nil` に戻る。

## Discussion
`scrollViewForTouches` の結果を弱参照で保持し、getter で返す。

## References
- [`WKHighlightLongPressGestureRecognizer.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKHighlightLongPressGestureRecognizer.h#L32)
- [`WKHighlightLongPressGestureRecognizer.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKHighlightLongPressGestureRecognizer.mm#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
