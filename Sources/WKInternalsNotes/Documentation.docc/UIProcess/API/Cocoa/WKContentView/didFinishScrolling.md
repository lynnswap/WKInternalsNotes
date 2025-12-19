# ``WKInternalsNotes/WKContentView/didFinishScrolling()``

スクロール終了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)didFinishScrolling;
```

## Discussion
`_needsScrollend` を立てたうえで `_didEndScrollingOrZooming` を呼び出す。

## References
- [`WKContentView.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L86)
- [`WKContentView.mm#L745`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L745)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
