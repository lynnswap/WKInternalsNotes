# ``WKInternalsNotes/WKImmediateActionController/didPerformImmediateActionHitTest(_:contentPreventsDefault:userData:)``

即時アクションのヒットテスト結果を受け取る。

## Objective-C Declaration
```objective-c
- (void)didPerformImmediateActionHitTest:(const WebKit::WebHitTestResultData&)hitTestResult contentPreventsDefault:(BOOL)contentPreventsDefault userData:(API::Object*)userData;
```

## Discussion
状態が `Pending` の場合に結果を保持し、`_updateImmediateActionItem` を呼んだ後 `_cancelImmediateActionIfNeeded` を実行する。

## References
- [`WKImmediateActionController.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.h#L82)
- [`WKImmediateActionController.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
