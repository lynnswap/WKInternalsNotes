# ``WKInternalsNotes/WKTextInteractionWrapper/reset()``

内部状態をリセットする。

## Objective-C Declaration
```objective-c
- (void)reset;
```

## Discussion
`shouldRestoreEditMenuAfterOverflowScrolling` を `NO` に戻し、`_hideEditMenuScope` を破棄する。

## References
- [`WKTextInteractionWrapper.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L64)
- [`WKTextInteractionWrapper.mm#L369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L369)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
