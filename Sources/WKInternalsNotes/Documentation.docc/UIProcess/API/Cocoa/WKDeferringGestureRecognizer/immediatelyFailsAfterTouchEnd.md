# ``WKInternalsNotes/WKDeferringGestureRecognizer/immediatelyFailsAfterTouchEnd``

タッチ終了直後に失敗扱いにするかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL immediatelyFailsAfterTouchEnd;
```

## Default Value
`NO`。

## Discussion
`touchesEnded:` 内で `YES` の場合、`state` を `Failed` に設定する。

## References
- [`WKDeferringGestureRecognizer.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L53)
- [`WKDeferringGestureRecognizer.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
