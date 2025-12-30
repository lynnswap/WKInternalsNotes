# ``WKInternalsNotes/WKImmediateActionController/initWithPage(_:view:viewImpl:recognizer:)``

即時アクション用の状態を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithPage:(std::reference_wrapper<WebKit::WebPageProxy>)page view:(NSView *)view viewImpl:(std::reference_wrapper<WebKit::WebViewImpl>)viewImpl recognizer:(NSImmediateActionGestureRecognizer *)immediateActionRecognizer;
```

## Discussion
`_page` / `_view` / `_viewImpl` / `_immediateActionRecognizer` を保持し、`_type` を `kWKImmediateActionNone`、`_hasActiveImmediateAction` を `NO` に初期化する。

## References
- [`WKImmediateActionController.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.h#L80)
- [`WKImmediateActionController.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
