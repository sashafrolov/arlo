import React from 'react'
import { render, fireEvent, wait } from '@testing-library/react'
import ResetButton from './ResetButton'
import { api, toaster } from '../utilities'

const apiMock = api as jest.Mock<ReturnType<typeof api>, Parameters<typeof api>>
const toasterMock = toaster as jest.Mock<
  ReturnType<typeof toaster>,
  Parameters<typeof toaster>
>

jest.mock('../utilities')
apiMock.mockImplementationOnce(async () => '{}')
toasterMock.mockImplementation(() => false)

describe('ResetButton', () => {
  it('renders', () => {
    const updateAuditMock = jest.fn()
    const { container } = render(
      <ResetButton electionId="1" updateAudit={updateAuditMock} />
    )
    expect(container).toMatchSnapshot()
  })

  it('renders disabled', () => {
    const updateAuditMock = jest.fn()
    const { container } = render(
      <ResetButton electionId="1" updateAudit={updateAuditMock} />
    )
    expect(container).toMatchSnapshot()
  })

  it('posts to /audit/reset and calls updateAudit', async () => {
    const updateAuditMock = jest.fn()
    const wrapper = document.createElement('div')
    wrapper.setAttribute('id', 'reset-button-wrapper')

    const { getByText } = render(
      <ResetButton electionId="1" updateAudit={updateAuditMock} />,
      { container: document.body.appendChild(wrapper) }
    )

    fireEvent.click(getByText('Clear & Restart'), { bubbles: true })

    await wait(() => {
      expect(apiMock).toBeCalledTimes(1)
      expect(toasterMock).toBeCalledTimes(1)
      expect(updateAuditMock).toBeCalledTimes(1)
    })
  })
})
