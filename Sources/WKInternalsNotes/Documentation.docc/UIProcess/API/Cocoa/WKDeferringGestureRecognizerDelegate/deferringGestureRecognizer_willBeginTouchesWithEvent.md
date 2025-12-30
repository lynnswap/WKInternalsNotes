# ``WKInternalsNotes/WKDeferringGestureRecognizerDelegate/deferringGestureRecognizer(_:willBeginTouchesWithEvent:)``

タッチ開始時にジェスチャの遅延可否を判定する。

## Objective-C Declaration
```objective-c
- (WebKit::ShouldDeferGestures)deferringGestureRecognizer:(WKDeferringGestureRecognizer *)deferringGestureRecognizer willBeginTouchesWithEvent:(UIEvent *)event;
```

## Discussion
ジェスチャの追跡を開始し、画像解析で操作可能な項目がある場合は `ShouldDeferGestures::No` を返す。慣性スクロールの割り込みがある場合も `No`、それ以外は `Yes` を返す。

## References
- [`WKDeferringGestureRecognizer.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L40)
- [`WKContentViewInteraction.mm#L10380`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10380)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
