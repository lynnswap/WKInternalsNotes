# ``WKInternalsNotes/WKContentView/resignFirstResponderForWebView()``

WebView の first responder を手放す。

## Objective-C Declaration
```objective-c
- (BOOL)resignFirstResponderForWebView;
```

## Discussion
`_resigningFirstResponder` を立てて編集終了処理を行い、必要なら `super` の `resignFirstResponder` を呼ぶ。成功時は activity state 更新やイベントハンドラの整理を行う。

## References
- [`WKContentViewInteraction.h#L759`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L759)
- [`WKContentViewInteraction.mm#L2121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2121)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
