# ``WKInternalsNotes/WKContentView/inputViewForWebView``

WebView 向けの inputView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *inputViewForWebView;
```

## Default Value
フォーカス要素が無い場合は `nil`。それ以外はカスタム入力ビューなどを優先して返す。

## Discussion
フォーカス要素が無い場合は `nil`。`_inputPeripheral` がある場合は `_zoomToRevealFocusedElement` と `_updateAccessory` を実行し、`customInputView` → `dataListTextSuggestionsInputView` → `assistantView` の順で返す。

## References
- [`WKContentViewInteraction.h#L729`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L729)
- [`WKContentViewInteraction.mm#L2939`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2939)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
