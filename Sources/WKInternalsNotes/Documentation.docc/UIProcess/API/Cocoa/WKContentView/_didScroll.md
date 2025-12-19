# ``WKInternalsNotes/WKContentView/_didScroll()``

スクロール発生時の内部処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didScroll;
```

## Discussion
コンテキストメニューヒント用コンテナの位置更新後、ロングプレスをキャンセルし、進行中のインタラクションを解除する。

## References
- [`WKContentViewInteraction.h#L824`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L824)
- [`WKContentViewInteraction.mm#L2759`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2759)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
