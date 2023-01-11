import type { ReactElement } from 'react'
import Layout from '@/components/admin/Layout'
import Join from '@/components/user/Join'
import type { NextPageWithLayout } from '@/pages/_app'

const Page: NextPageWithLayout = () => {
  return <Join/>
}

Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      {page}
    </Layout>
  )
}

export default Page