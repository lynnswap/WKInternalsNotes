# ``WKInternalsNotes/WKDeferringGestureRecognizerDelegate/deferringGestureRecognizer(_:shouldDeferOtherGestureRecognizer:)``

他のジェスチャを遅延するか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)deferringGestureRecognizer:(WKDeferringGestureRecognizer *)deferringGestureRecognizer shouldDeferOtherGestureRecognizer:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
タッチイベントで必ず失敗すべきジェスチャや WebView 外部のジェスチャ、`WKDeferringGestureRecognizer` 自身、`_touchEventGestureRecognizer`、キーボード解除ジェスチャなどは `NO` を返す。タッチ移動用デファラはパン/ピンチに限定し、その他は合成タップや遅延リセット対象かどうかで各デファラに割り当てる。

## References
- [`WKDeferringGestureRecognizer.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L40)
- [`WKContentViewInteraction.mm#L10423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
