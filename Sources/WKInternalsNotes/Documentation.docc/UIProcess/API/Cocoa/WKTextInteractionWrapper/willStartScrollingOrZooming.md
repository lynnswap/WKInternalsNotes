# ``WKInternalsNotes/WKTextInteractionWrapper/willStartScrollingOrZooming()``

スクロール/ズーム開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)willStartScrollingOrZooming;
```

## Discussion
`_textInteractionAssistant willStartScrollingOrZooming` を呼び、`USE(BROWSERENGINEKIT)` では edit menu の表示状態を保持して一旦閉じる。

## References
- [`WKTextInteractionWrapper.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L53)
- [`WKTextInteractionWrapper.mm#L375`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L375)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
