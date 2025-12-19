# ``WKInternalsNotes/WKTextInteractionWrapper/didEndScrollingOverflow()``

オーバーフロースクロール終了で edit menu を復帰する。

## Objective-C Declaration
```objective-c
- (void)didEndScrollingOverflow;
```

## Discussion
`_hideEditMenuScope` を破棄し、edit menu 抑制を解除する。

## References
- [`WKTextInteractionWrapper.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L42)
- [`WKTextInteractionWrapper.mm#L364`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L364)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
