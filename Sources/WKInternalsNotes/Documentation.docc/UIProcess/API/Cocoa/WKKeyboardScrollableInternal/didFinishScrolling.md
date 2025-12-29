# ``WKInternalsNotes/WKKeyboardScrollableInternal/didFinishScrolling()``

スクロール完了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)didFinishScrolling;
```

## Discussion
delegate が `keyboardScrollViewAnimatorDidFinishScrolling:` に応答できる場合は通知し、`_scrollView` を `nil` にする。

## References
- [`WKKeyboardScrollingAnimator.mm#L757`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L757)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
